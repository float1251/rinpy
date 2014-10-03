==================
rinpy
==================
rinpy is BDD Test Framework for python. inspired mocha.

**Currently Under Development.**


Sample
----------
::

    @describe("A")
    class TestA:

        @it("hello return  Hello")
        def test(self):
            assert "Hello" == hello() 

        @it("world return World")
        def it(self):
            assert "World" == world()

..
    How to install
    ----------------
    .. code-block::
        
        pip install rinpy


..
    How to use
    ---------------
    * class name contain Test, and method name contain test.
