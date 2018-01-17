package com.bruce.scorecv

import java.io.File

import org.bytedeco.javacpp.opencv_imgcodecs._
import OpenCVUtils._

/**
 * Example for section "Using the Strategy pattern in algorithm design" in Chapter 3.
 * The pattern encapsulates an algorithm into a separate class
 *
 * The original example in the book is using "C++ API". Calls here use "C API" supported by JavaCV.
 */
object ScoreDetector extends App {

  // Create image processor object
  val colorDetector = new ColorDetector

  // Read input image
  val src = loadAndShowOrExit(new File("data/SingleScore.png"), IMREAD_COLOR)

  // Set the input parameters
  colorDetector.colorDistanceThreshold = 100
  // here white characters
  colorDetector.targetColor = new ColorRGB(255, 255, 255)

  // Process that input image and display the result
  val dest = colorDetector.process(src)
  show(dest, "result")
}