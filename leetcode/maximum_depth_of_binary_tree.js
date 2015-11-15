// https://leetcode.com/problems/maximum-depth-of-binary-tree/

/**
 * Definition for binary tree
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @returns {number}
 */
var maxDepth = function(root) {
    return root === null ? 0 : 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
};