

fun minimumSwaps(arr: Array<Int>): Int {
  var moves = 0
  var i = 0
  while (i < arr.size) {
    if (arr[i] != i + 1) {
      arr[arr[i] - 1] = arr[i].also { arr[i] = arr[arr[i] - 1] }
      moves++
    }
    if (arr[i] == i + 1) {
      i++
    }
  }
  return moves
}
