1、Unittest基础使用
    1.1 test case:  测试用户
    1.2 test suite： 多个测试用例的集合，测试套件或测试计划
    1.3 testLoader： 用例加载
    1.4 test runner：用例执行
    1.5 test fixture: 一个测试用例的初始化准备及环境还原，主要是setUp()
        setDown()方法

Unittest测试框架使用步骤：
1、用户import语句引入unittest模块
2、让所有执行测试的类都继承与testCase类，可以将TestCase看成是对特定类进行测试
3、setUp()方法中进行测试前的初始化工作，Teardown()方法中执行测试后的清除工作，它们都是TestCase中的方法
4、编写测试的方法最好以test开头（可以直接运行） def test_add(self)、def test_sub(self)等，可以编写多个测试用例对被测对象进行测试
5、在编写测试方法过程中，使用TestCase class 提供的方法测试功能点，比如： assertEqual等
6、调用unittest.main()方法运行所有以test开头的方法


实战2：
业务类--》把业务类里面的操作封装成方法

测试类
步骤1： 编写一个计算器的业务类 calc.py
步骤2： 编写unitest测试用例


2、Unittest常用断言
什么是断言： 判断结果是否正确
怎么用：
在什么地方用： 在核心业务执行使用


3、unittest框架默认根据ACSII码的顺序加载测试用例，数字与字母的顺序为：0～9，A～Z，a～z
3.1 默认执行顺序


4、忽略用例
开发没有修改完成，或者是暂时不能执行的情况
在执行测试脚本的时候，可能会有某几条用例本次不想执行，
但是又不想删不想注释，unittest通过忽略部分测试用例不执行的方式，
分无条件忽略和有条件忽略，通过装饰器实现所描述的场景，提供的装饰器如下：
a、unittest.skip(reason):强制跳转，reason是跳转原因
b、unittest.skiplf(condition,reason): condition为True的时候跳转
c、unittest.skipUnless(condition,reason): condition为False的时候跳转
b、unittest.expectedFailure: 标记该测试预期为失败，如果该测试方法运行失败，则该测试不算做失败


5、主套件---子套件---用例
  方法一： 用unittest.TestSuite() 实例化测试套件对象后，
内部的addTest()方法对测试类内部的测试案例进行逐一添加
  
  方法二： 用unittest.TestSuite() 实例化测试套件对象后，
使用MakeSuite()，一次性将整个测试类文件下所有测试用例到suite中去

  方法三： unittest 提供一个TestLoader类用于自动创建一个测试集并
把单个测试放入到测试集中。TestLoader 自动运行以test开头的测试方法

  方法四：用unittest.TestSuite() 实例化测试套件对象后，
内部的addTests()方法可以把多个子测试集合进行整合到一个大的测试集合中

  方式五： 当测试用例存放在多个不同子目录下，我们用之前的把用例加载到测试集合
中的方式还是不太方便，需要不断的去导入和添加测试用例模块，此时可以通过discover()
方法来实现

加载用例的四层
1、suite下的用例
2、py模块下的用例
3、测试类class下的用例
4、test开头的测试方法


方式五： 此时可以通过discover()方法来实现
步骤1： 新建测试模块test_one，在里面添加测试类，在test_one里面新建test_two包
也添加测试类

步骤2： 编写用例执行文件，run_case.py，使用discover()来加载test_one的
里面的所有用例

补充：使用discover()方式，不执行用例的处理
1、注释不执行的用例
2、在test_case方法前假not，这样用例就是not开头了
3、忽略用例
4、在test_xx.py文件名not_test_xx.py


测试报告的生成及优化

方式一： 用unittest.main()执行生成

方式二： 使用TextTestRunner执行测试用例集，TextTestRunner 有三个参数，它们都是有默认参数：
1、verbosity 分别三个级别：0 1 2  它们输出的测试报告详细过程不同。2 最详细
2、stream 关系着测试报告的位置，如果默认为None的话，测试报告会输出到控制台
3、descripions 测试报告的描述

方式三：
  使用第三方 HTMLTestRunner 执行测试用例集，它们可以输出网页版测试报告

优化报告：
1、加用例备注
2、日志文件名覆盖的处理

Python+selenuim+unittest
