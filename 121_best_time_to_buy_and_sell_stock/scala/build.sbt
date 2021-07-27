ThisBuild / scalaVersion := "2.13.4"
ThisBuild / organization := "co.mrzzy"

lazy val root = (project in file("."))
  .settings(
    name := "Best Time to buy and sell stocks",
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.9" % "test"
  )
