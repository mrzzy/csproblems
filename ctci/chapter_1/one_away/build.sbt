/*
 * Cracking the Coding Interview
 * Chapter 1: One Away
 * sbt build
 */

ThisBuild / scalaVersion := "2.13.4"
ThisBuild / organization := "ctci.chapter1"

lazy val root = (project in file("."))
  .settings(
    name := "One Away",
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.9" % "test"
  )
