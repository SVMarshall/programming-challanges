
import java.util.*

fun arrayManipulation(n: Int, queries: Array<Array<Int>>): Long {
  val ops = IntArray(n)
  for (query in queries) {
    val from = query[0] - 1
    val to = query[1] - 1
    val value = query[2]
    ops[from] += value
    if (to < n - 1) ops[to + 1] -= value
  }
  var currentHigh = 0L
  var maxHigh = 0L
  for (op in ops) {
    currentHigh += op
    maxHigh = maxOf(maxHigh, currentHigh)
  }
  return maxHigh
}

fun main(args: Array<String>) {
  val scan = Scanner(System.`in`)
  val nm = scan.nextLine().split(" ")
  val n = nm[0].trim().toInt()
  val m = nm[1].trim().toInt()
  val queries = Array<Array<Int>>(m, { Array<Int>(3, { 0 }) })
  for (i in 0 until m) {
    queries[i] = scan.nextLine().split(" ").map{ it.trim().toInt() }.toTypedArray()
  }
  val result = arrayManipulation(n, queries)
  println(result)
}
