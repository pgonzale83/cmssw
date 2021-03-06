/*----------------------------------------------------------------------

Test program for edm::propagate_const class.

 ----------------------------------------------------------------------*/

#include <cppunit/extensions/HelperMacros.h>
#include <memory>
#include "FWCore/Utilities/interface/get_underlying_safe.h"

class test_propagate_const: public CppUnit::TestFixture
{
CPPUNIT_TEST_SUITE(test_propagate_const);

CPPUNIT_TEST(test);

CPPUNIT_TEST_SUITE_END();
public:
  void setUp(){}
  void tearDown(){}

  void test();
};

///registration of the test so that the runner can find it
CPPUNIT_TEST_SUITE_REGISTRATION(test_propagate_const);

namespace {
   class ConstChecker {
   public:
      int value() { return 0;}
      
      int const value() const { return 1;}
      
   };
}


void test_propagate_const::test()
{
   {
      ConstChecker checker;
      edm::propagate_const<ConstChecker*> pChecker(&checker);

      CPPUNIT_ASSERT(0 == pChecker.get()->value());
      CPPUNIT_ASSERT( pChecker.get()->value() == pChecker->value());
      CPPUNIT_ASSERT( pChecker.get()->value() == (*pChecker).value());
      CPPUNIT_ASSERT(0 == get_underlying_safe(pChecker)->value());

      const edm::propagate_const<ConstChecker*> pConstChecker(&checker);

      CPPUNIT_ASSERT(1 == pConstChecker.get()->value());
      CPPUNIT_ASSERT( pConstChecker.get()->value() == pConstChecker->value());
      CPPUNIT_ASSERT( pConstChecker.get()->value() == (*pConstChecker).value());
      CPPUNIT_ASSERT(1 == get_underlying_safe(pConstChecker)->value());
   }
   
   {
      auto checker = std::make_shared<ConstChecker>();
      edm::propagate_const<std::shared_ptr<ConstChecker>> pChecker(checker);
      
      CPPUNIT_ASSERT(0 == pChecker.get()->value());
      CPPUNIT_ASSERT( pChecker.get()->value() == pChecker->value());
      CPPUNIT_ASSERT( pChecker.get()->value() == (*pChecker).value());
      CPPUNIT_ASSERT(0 == get_underlying_safe(pChecker)->value());

      const edm::propagate_const<std::shared_ptr<ConstChecker>> pConstChecker(checker);
      
      CPPUNIT_ASSERT(1 == pConstChecker.get()->value());
      CPPUNIT_ASSERT( pConstChecker.get()->value() == pConstChecker->value());
      CPPUNIT_ASSERT( pConstChecker.get()->value() == (*pConstChecker).value());
      CPPUNIT_ASSERT(1 == get_underlying_safe(pConstChecker)->value());
   }
   
   {
      auto checker = std::make_unique<ConstChecker>();
      edm::propagate_const<std::unique_ptr<ConstChecker>> pChecker(std::move(checker));
      
      CPPUNIT_ASSERT(0 == pChecker.get()->value());
      CPPUNIT_ASSERT( pChecker.get()->value() == pChecker->value());
      CPPUNIT_ASSERT( pChecker.get()->value() == (*pChecker).value());
      CPPUNIT_ASSERT(0 == get_underlying_safe(pChecker)->value());

      const edm::propagate_const<std::unique_ptr<ConstChecker>> pConstChecker(std::make_unique<ConstChecker>());
      
      CPPUNIT_ASSERT(1 == pConstChecker.get()->value());
      CPPUNIT_ASSERT( pConstChecker.get()->value() == pConstChecker->value());
      CPPUNIT_ASSERT( pConstChecker.get()->value() == (*pConstChecker).value());
   }

}
