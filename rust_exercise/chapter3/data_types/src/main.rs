fn main() {
    // Rust is a statically typed language

    // Scalar Types
    //
    let old: u8 = 255;
    println!("old is {}", old);

    // Numenic operations
    let quotient = 56.7 / 32.2;
    let floored = 2 / 3; // Results in 0
    println!("quotient is {} and floored is {}", quotient, floored);


    // Compound types
    // Tuple
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (_x, y, _z) = tup;
    println!("The value of y is: {y}");
    let five_hundrad = tup.0;
    println!("The value of five_hundrad is : {}", five_hundrad);

    // Array
    // Unlike a tuple, every element of an array must have the same type.
    let a: [u32;5] = [3;5];
    println!("the second element of a is {}", a[2]);

}
