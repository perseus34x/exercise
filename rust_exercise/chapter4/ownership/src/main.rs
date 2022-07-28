fn main() {
    let mut s = String::from("hello");
    s.push_str(", world!"); // push_str() appends a literal to a String
    println!("{}", s); // This will print `hello, world!`

    // Move
    let x = 5;
    let y = x;
    println!("x is {x} and y is {y}");
    
    let s1 = String::from("hello");
    let _s2 = s1;
    //println!("s1 is {s1} and s2 is {s2}");
    // this will cause an error

    // Clone
    let s1 = String::from("hello");
    let s2 = s1.clone();
    println!("s1 = {}, s2 = {}", s1, s2);

    //Ownership and Functions
    let s = String::from("Super star");  // s comes into scope
    takes_ownership(s);             // s's value moves into the function...
    // ... and so is no longer valid here

    let x = 6;                      // x comes into scope
    makes_copy(x);                  // x would move into the function,

    // Return Values and Scope
    let s1 = String::from("hello world");
    let (s2, len) = calculate_length(s1);
    println!("The length of '{}' is {}.", s2, len);

}

fn takes_ownership(some_string: String) { // some_string comes into scope
    println!("{}", some_string);
} // Here, some_string goes out of scope and `drop` is called. The backing
  // memory is freed.

fn makes_copy(some_integer: i32) { // some_integer comes into scope
    println!("{}", some_integer);
} // Here, some_integer goes out of scope. Nothing special happens.

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() returns the length of a String

    (s, length)
}
