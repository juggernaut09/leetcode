impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {
        let mut a: i64 = 0;
        let mut b: i64 = (c as f64).sqrt() as i64;
        let mut curr_sum: i64;
        while a <=b {
            curr_sum = a.pow(2) + b.pow(2);
            if curr_sum == (c as i64) {
                return true;
            } else if curr_sum < (c as i64){
                a += 1;
            } else {
                b -= 1;
            }
        
        }

        false
    }
}