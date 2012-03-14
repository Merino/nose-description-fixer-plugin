from nose.plugins import Plugin

class DescriptionFixer(Plugin):
    """
    Test description fixer plugin.
    When you use the verbose flag (-v) on a testrun, test functions that include
    a docstring will show this instead of the function name with parameters.
    This is especially annoying for generative tests where you can get a huge
    block of test results that look identical.

    """
    # a lot of the boilerplate code here is just taken right out of the builtin
    # capture plugin

    enabled = True
    env_opt = 'NOSE_NODESCRIPTIONFIXER'
    name = 'descriptionfixer'
    score = 2000

    def __init__(self):
        Plugin.__init__(self)

    def options(self, parser, env):
        parser.add_option("--nodescriptionfixer",
                          action="store_false",
                          default=not env.get(self.env_opt),
                          dest="fixdescription",
                          help=("Don't fix test descriptions"),
                         )

    def configure(self, options, conf):
        self.conf = conf
        if not options.fixdescription:
            self.enabled = False

    def describeTest(self, test):
        return False # this is where the magic happens

