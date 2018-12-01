
import kotlin.collections.*

class FrequenciesMap {
  private val numberFrequencies = mutableMapOf<Int, Int>()
  private val frequenciesCounts = mutableMapOf<Int, Int>()

  fun insert(value: Int) {
    val newValueFrequency = insertOnNumberFrequencies(value)
    insertOnFrequenciesLists(newValueFrequency)
  }

  fun delete(value: Int) {
    val newValueFrequency = deleteOnNumberFrequencies(value)
    newValueFrequency?.let { deleteOnFrequenciesLists(it) }
  }

  fun check(freq: Int): Boolean {
    return frequenciesCounts.any { it.key == freq && it.value > 0}
  }

  private fun insertOnNumberFrequencies(value: Int): Int {
    val newValueFrequency = numberFrequencies[value]?.inc() ?: 1
    numberFrequencies[value] = newValueFrequency
    return newValueFrequency
  }

  private fun insertOnFrequenciesLists(newValueFrequency: Int) {
    frequenciesCounts[newValueFrequency - 1]?.let { frequenciesCounts[newValueFrequency - 1] = it - 1 }
    frequenciesCounts[newValueFrequency]
            ?.let { frequenciesCounts[newValueFrequency] = it + 1 }
            ?: run { frequenciesCounts[newValueFrequency] = 1 }
  }

  private fun deleteOnNumberFrequencies(value: Int): Int? {
    val newValueFrequency = numberFrequencies[value]?.dec()
    newValueFrequency?.let { numberFrequencies[value] = it }
    return newValueFrequency
  }

  private fun deleteOnFrequenciesLists(newValueFrequency: Int) {
    frequenciesCounts[newValueFrequency + 1] = frequenciesCounts[newValueFrequency + 1]!!.minus(1)
    frequenciesCounts[newValueFrequency] = frequenciesCounts[newValueFrequency]?.plus(1) ?: 1
  }

}

fun freqQuery(queries: Array<Array<Int>>): Array<Int> {
  val res = mutableListOf<Int>()
  val freqMap = FrequenciesMap()

  for (query in queries) {
    when (query[0]) {
      1 -> freqMap.insert(query[1])
      2 -> freqMap.delete(query[1])
      3 -> res += when(freqMap.check(query[1])) {true -> 1; false -> 0}
    }
  }

  return res.toTypedArray()
}

fun main(args: Array<String>) {
  val q = readLine()!!.trim().toInt()
  val queries = Array(q) { Array(2, { 0 }) }
  for (i in 0 until q) {
    queries[i] = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()
  }
  val ans = freqQuery(queries)
  println(ans.joinToString("\n"))
}
