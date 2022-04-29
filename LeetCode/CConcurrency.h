/*
并行编程
*/
#include <queue>
#include <chrono>
#include <mutex>
#include <thread>
#include <iostream>
#include <condition_variable>
#include <functional>
#include <thread>
#include <iostream>
using std::function;
using std::unique_lock;
namespace CConcurrency
{
    // https://leetcode.com/problems/building-h2o/
    // 1117. Building H2O
    /*
        有两类线程，氧气和氢气线程，编码实现控制这两个线程生成一个水分子。 限制：输出一个氧气必须等待两个氢气，同理以此类推……
        solution： 这又是一个线程同步问题。 通过一个信号量同步两个线程重新生成H和O。 两个变量记录生成的H、O个数。 达到一个水分子个数
        时，等待
    */
    class H2O
    {
    private:
        int count_h, count_o;
        std::mutex mtx;
        std::condition_variable cv;

    public:
        H2O()
        {
            count_h = count_o = 0;
        }

        void hydrogen(function<void()> releaseHydrogen)
        {
            while(true) {
                
            }
            releaseHydrogen();
        }

        void oxygen(function<void()> releaseOxygen)
        {

            // releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen();
        }
    };
    // https://leetcode.com/problems/print-zero-even-odd/
    // 1116. Print Zero Even Odd
    /* 有一个可以在控制台输出数字的函数，启动3个线程，分别输出0，奇数、偶数。
        实现一个类，给定数字n，输出偶数个结果： 0102..0n
    solution: 这是一个线程同步问题. 线程zero等待一个信号,允许它输出0; 这个信号由两个
    线程 even 和 odd 去修改; 输出完0后根据当前值切换信号，执行 even 或 odd 。
    这个切换需要枚举, 到底是哪个线程 zero or even 去工作。
    Runtime: 33 ms, faster than 52.04% of C++ online submissions for Print Zero Even Odd.
    Memory Usage: 6.9 MB, less than 82.16% of C++ online submissions for Print Zero Even Odd.
     */
    enum thread_to_go
    {
        zero = 0,
        odd = 1,
        even = 2
    };
    class ZeroEvenOdd
    {
    private:
        int n, current;
        bool output_zero;
        thread_to_go go;
        std::mutex mtx;
        std::condition_variable cv;

    public:
        ZeroEvenOdd(int n)
        {
            this->n = n;
            this->current = 0;
            go = thread_to_go::zero; // 先输出0
        }

        // printNumber(x) outputs "x", where x is an integer.
        void zero(function<void(int)> printNumber)
        {
            for (int i = 0; i < n; ++i)
            {
                std::unique_lock<std::mutex> lck(mtx);
                while (go != thread_to_go::zero)
                    cv.wait(lck); // 等待允许输出0
                printNumber(0);
                if (i % 2 != 0)
                {
                    go = thread_to_go::even;
                }
                else
                {
                    go = thread_to_go::odd;
                }
                cv.notify_all();
            }
        }

        void even(function<void(int)> printNumber)
        {
            for (int i = 2; i <= n; i += 2)
            {
                std::unique_lock<std::mutex> lck(mtx);
                while (go != thread_to_go::even)
                    cv.wait(lck); // 等待允
                printNumber(i);
                go = thread_to_go::zero;
                cv.notify_all();
            }
        }

        void odd(function<void(int)> printNumber)
        {
            for (int i = 1; i <= n; i += 2)
            {
                std::unique_lock<std::mutex> lck(mtx);
                while (go != thread_to_go::odd)
                    cv.wait(lck); // 等待允
                printNumber(i);
                go = thread_to_go::zero;
                cv.notify_all();
            }
        }
    };
    // https://leetcode.com/problems/print-foobar-alternately/
    // 1115. Print FooBar Alternately
    /*
        两个线程，按给定的个数，输出n次 foobar。 其中一个线程输出 foo, 另一个输出bar
        这是两个线程同步的问题，没有多线程竞争。
        solution： 用一个信号量就可以了，初始化 信号量 s 允许输出 foo，不许输出 bar。 输出完 foo 后设置允许输出 bar 不许输出 foo。
        Runtime: 150 ms, faster than 45.64% of C++ online submissions for Print FooBar Alternately.
        Memory Usage: 8.3 MB, less than 30.38% of C++ online submissions for Print FooBar Alternately.
    */
    class FooBar
    {
    private:
        int n;
        std::mutex mtxa;
        bool go_foo;
        std::condition_variable cv1;

    public:
        FooBar(int n)
        {
            this->n = n;
            go_foo = true;
        }

        void foo(function<void()> printFoo)
        {
            for (int i = 0; i < n; ++i)
            {
                unique_lock<std::mutex> lck(mtxa);
                cv1.wait(lck, [this]()
                         { return go_foo; });
                // printFoo() outputs "foo". Do not change or remove this line.
                printFoo();
                go_foo = false;
                cv1.notify_one(); // 唤醒输出 bar
            }
        }

        void bar(function<void()> printBar)
        {
            for (int i = 0; i < n; ++i)
            {
                unique_lock<std::mutex> lck(mtxa);
                cv1.wait(lck, [this]()
                         { return !go_foo; });
                // printBar() outputs "bar". Do not change or remove this line.
                printBar();
                go_foo = true;
                cv1.notify_one();
            }
        }
    };

    // https://leetcode.com/problems/print-in-order/
    // 1114. Print in Order
    /*The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
    // solution: 使用两个条件变量
    Runtime: 376 ms, faster than 13.96% of C++ online submissions for Print in Order.
    Memory Usage: 7.2 MB, less than 64.53% of C++ online submissions for Print in Order.
    */
    class Foo
    {
    private:
        std::condition_variable cv1, cv2;
        bool notify_a, notify_b;
        std::mutex mtxa, mtxb;

    public:
        Foo()
        {
            notify_a = false;
            notify_b = false;
        }

        void first(function<void()> printFirst)
        {

            // printFirst() outputs "first". Do not change or remove this line.
            // 生产者a
            std::unique_lock<std::mutex> lck(mtxa);
            printFirst();
            notify_a = true;
            cv1.notify_one();
        }

        void second(function<void()> printSecond)
        {

            // printSecond() outputs "second". Do not change or remove this line.
            // 生产者b等待a
            std::unique_lock<std::mutex> lck(mtxa);
            std::unique_lock<std::mutex> lck1(mtxb);
            while (!notify_a)
                cv1.wait(lck);
            printSecond();
            notify_b = true;
            cv2.notify_one();
        }

        void third(function<void()> printThird)
        {

            // printThird() outputs "third". Do not change or remove this line.
            std::unique_lock<std::mutex> lck(mtxb);
            while (!notify_b)
                cv2.wait(lck);
            printThird();
        }
    };
};