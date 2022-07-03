ThisBuild / scalaVersion := "2.13.4"
ThisBuild / organization := "leetcode"

lazy val root = (project in file("."))
  .settings(
    name := "153. Find Minimum in Rotated Sorted Array",
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.9" % "test"
  )
