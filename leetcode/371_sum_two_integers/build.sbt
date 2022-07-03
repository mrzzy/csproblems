/*
 * Leetcode
 * 371. Sum of Two Integers
 * SBT Build
*/

ThisBuild / scalaVersion := "2.13.4"
ThisBuild / organization := "co.mrzzy"

lazy val root = (project in file("."))
  .settings(
    name := "371. Sum of Two Integers",
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.9" % "test"
  )
