'''
doc: https://pyopenssl.org/en/stable/api
install : pip install pyOpenSSL 
'''
import OpenSSL
from OpenSSL import SSL
import socket
from OpenSSL import crypto
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
import traceback

# hostname = 'www.hellofreedom.top'
# port = 443

# # Create a socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect to the server
# sock.connect((hostname, port))

# pin 服务器的公钥
pin_key = b'-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEv+oeaOc66EQI0PTilxT9ZfZspTuW\nfDc9+pJXSxU7qzmw3bEaygO8opo29UOELv3biVYts0BOJBgU/f4xNiSwfQ==\n-----END PUBLIC KEY-----\n'

class SslClientWrap():
    def __init__(self, server, port, method=SSL.TLS_CLIENT_METHOD, max_version=0) -> None:
        '''
        @param      server      连接的server
        @param      port        连接的端口
        @param      method      构造 Context 的方法： client or server
        @param      max_version   最大支持的协议版本; OpenSSL.SSL.TLS1_2_VERSION
        '''
        self.server     =   server
        self.port       =   port
        self.context    =   SSL.Context(method) # 根据 method 构造一个context
        self.context.set_max_proto_version(max_version) # 设置最大支持的 tls 协议版本； 可以不设置。
        self.context.set_verify(SSL.VERIFY_PEER, self.verify_certificate)   # 注册验证回调 以及 验证 peer 的方式
        self.context.set_info_callback(self.info_callback)
        self.context.set_keylog_callback(self.keylog_callback)  # 注册 key log， 记录协商的秘钥
        # Create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        self.sock.connect((server, port))
        self.ssl_sock = SSL.Connection(self.context, self.sock) # 根据 context 和 socket 构造 ssl connection 
        self.__handshake() # ssl 握手
    
    def __handshake(self):
        self.ssl_sock.set_connect_state()
        try:
            self.ssl_sock.do_handshake()
        except Exception as e:
            print(e)

    def close(self):
        self.ssl_sock.shutdown()
        self.ssl_sock.close()


    def dump_info(self):
        context = self.context
        print("verify depth: ", context.get_verify_depth())
        print("verify mode: ", context.get_verify_mode())
        cert = self.ssl_sock.get_peer_certificate()

        # Print the certificate details
        print("Certificate subject:")
        print(cert.get_subject())

        print("\nCertificate issuer:")
        print(cert.get_issuer())

        print("\nCertificate version:")
        print(cert.get_version())

        print("\nCertificate serial number:")
        print(cert.get_serial_number())
    
    def ssl_pin(self, pubkey):
        if pubkey == pin_key:
            print("************* ssl pin verify ok")
            return
        raise Exception("ssl cert not desired")
        

    def verify_certificate(self, conn, cert, errnum, depth, ok):
        '''
        会从 CA 的证书一直回调到 subject 的证书, depth从大到小最后为 0 就是subject的证书.
        若该函数返回0， 则握手失败
        '''
        # Implement your verification logic here
        # Return True if the certificate is valid, or False otherwise
        # Print the certificate details
        print("进行自定义证书校验 depth = {}".format(depth))
        print("1.Certificate subject:")
        print(cert.get_subject())

        print("\n2.Certificate issuer:")
        print(cert.get_issuer())

        print("\n3.Certificate version:")
        print(cert.get_version())

        print("\n4.Certificate serial number:")
        print(cert.get_serial_number())

        print("\n4.public key is :")
        pubkey:crypto.PKey = cert.get_pubkey()
        pubkey  =   pubkey.to_cryptography_key()
        print("pubkey type is {}".format(type(pubkey)))
        try:
            key_pem = pubkey.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
            print("PEM encoding\n", key_pem)
            if depth == 0:
                self.ssl_pin(key_pem)

            key_der = pubkey.public_bytes(Encoding.DER, PublicFormat.PKCS1)
            print("DER encoding\n", key_der)
        except:
            print(traceback.format_exc())

        print("\n5.ok= ", ok)
        if not ok:
            ok = 1
        return ok

    def info_callback(self, conn:SSL.Connection, caller, prev_ret):
        '''
        tls handshake 时不时调用该回调
        '''
        # print("info callback conn is :" + str(dir(conn)))
        try:
            print("client_random: ",bytearray(conn.client_random()).hex())
        except:
            pass

    def keylog_callback(self, conn, key:bytes):
        print("Keylogger called type(key) = {}" .format( type(key)))
        print(key)

    def say_hello(self):
        try:
            self.ssl_sock.write("GET / HTTP1.1")
            pass
        except Exception as e:
            print(e)

    def recv(self):
        data = self.ssl_sock.read(100)
        print("recv data: ", bytearray(data).hex())

# tls 1.2 
client = SslClientWrap('www.hellofreedom.top', 443,SSL.TLS_CLIENT_METHOD, SSL.TLS1_2_VERSION)
# tls 1.3 
# client = SslClientWrap('www.hellofreedom.top', 443,SSL.TLS_CLIENT_METHOD, SSL.TLS1_3_VERSION)
client.dump_info()
# client.say_hello()
# client.recv()
client.close()
exit(0)

def verify_certificate(conn, cert, errnum, depth, ok):
    # Implement your verification logic here
    # Return True if the certificate is valid, or False otherwise
    # Print the certificate details
    print("进行自定义证书校验")
    print("1.Certificate subject:")
    print(cert.get_subject())

    print("\n2.Certificate issuer:")
    print(cert.get_issuer())

    print("\n3.Certificate version:")
    print(cert.get_version())

    print("\n4.Certificate serial number:")
    print(cert.get_serial_number())

    print("\n5.ok= ", ok)
    if not ok:
        ok = 1
    return ok

def info_callback(conn, caller, prev_ret):
    '''
    tls handshake 时不时调用该回调
    '''
    print("info callback conn is :" + dir(conn))

def keylog_callback(conn, key:bytes):
    print("Keylogger called type(key) = " + type(key))
    print(dir(key))

#---------- 
# Create an SSL context
# context = SSL.Context(SSL.TLSv1_2_METHOD)       # 定义构造新 ssl 连接时的 参数
context = SSL.Context(SSL.TLS_CLIENT_METHOD)       # 定义构造新 ssl 连接时的 参数

context.set_verify(SSL.VERIFY_PEER, verify_certificate)     # 设置证书验证回调
context.set_info_callback(info_callback)
context.set_keylog_callback(keylog_callback)

# context.load_verify_locations(cafile="path/to/root/certificates.pem") # 加载信任的根证书
# context.load_default_certs()    # 加载系统内置的证书

print("verify depth: ", context.get_verify_depth())
print("verify mode: ", context.get_verify_mode())

# Wrap the socket with the SSL context
ssl_sock = SSL.Connection(context, sock)

# Perform the SSL handshake
ssl_sock.set_connect_state()
try:
    ssl_sock.do_handshake()
except Exception as e:
    print(e)



# Get the server's certificate
cert = ssl_sock.get_peer_certificate()

# Print the certificate details
print("Certificate subject:")
print(cert.get_subject())

print("\nCertificate issuer:")
print(cert.get_issuer())

print("\nCertificate version:")
print(cert.get_version())

print("\nCertificate serial number:")
print(cert.get_serial_number())

# ...add more certificate details as needed


ssl_sock.shutdown()
ssl_sock.close()

