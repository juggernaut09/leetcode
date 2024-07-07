impl Solution {
    pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut consumed: i32 = 0;
        let mut numbottles: i32 = num_bottles;
        
        while numbottles >= num_exchange {
            consumed += num_exchange;
            numbottles -= num_exchange;
            numbottles += 1;
        }

        consumed + numbottles
    }
}