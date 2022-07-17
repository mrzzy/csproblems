/*
 * CSProblems
 * LeetCode
 * 481. Magical String
 *
*/

ThisBuild / scalaVersion := "2.13.7"
ThisBuild / organization := "co.mrzzy"

lazy val solution = (project in file("."))
  .settings(
    name := "solution",
    libraryDependencies += "org.scalatest" %% "scalatest-funsuite" % "3.2.12" % Test,
  )
