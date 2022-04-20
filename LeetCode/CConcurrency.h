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
using std::function;
using std::unique_lock;
namespace CConcurrency
{
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