/// Time in seconds.
///
/// # Example
///
/// ```
/// let s = Second::new(42);
/// assert_eq!(42, s.value());
/// ```
#[derive(Debug,Default)]
pub struct Second {
    value: u64
}

impl Second {
    // Constructs a new instance of [`Second`].
    // Note this is an associated function - no self.
    pub fn new(value: u64) -> Self {
        Self { value }
    }

    /// Returns the value in seconds.
    pub fn value(&self) -> u64 {
        self.value
    }
}

//impl Default for Second {
//    fn default() -> Self {
//        Self { value: 0 }
//    }
//}

fn main() {
    let sec: Second = Second{value:1};
    println!("sec is {:?}", sec);
}
