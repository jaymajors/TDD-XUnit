class TestCase:
  def __init__(self, name):
    self.name = name

  def setUp(self):
    pass

  def run(self):
    self.setUp()
    method = getattr(self, self.name)
    method()

class WasRun(TestCase):
  def __init__(self, name):
    self.wasRun = None
    self.wasSetUp = None
    TestCase.__init__(self, name)

  def testMethod(self):
    self.wasRun = 1

  def setUp(self):
    self.wasSetUp = 1
    self.wasRun = None

class TestCaseTest(TestCase):
  
  def setUp(self):
    self.test = WasRun("testMethod")

  def testSetUp(self):
    test.run()
    assert(test.wasSetUp)
  
  def testRunning(self):
    test.run()
    assert(test.wasRun)


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
