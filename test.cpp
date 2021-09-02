#include <gtest/gtest.h>

TEST(Foo, SumSucceed)
{
  EXPECT_EQ(2, 1 + 1);
}

TEST(Bar, SumFail)
{
  EXPECT_EQ(2, 3);
}