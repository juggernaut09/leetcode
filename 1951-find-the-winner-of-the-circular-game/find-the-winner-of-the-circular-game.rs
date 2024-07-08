impl Solution {
    pub fn find_the_winner(n: i32, k: i32) -> i32 {
        (2..=n).fold(0, |s, n| (s+k) % n) + 1
    }
}