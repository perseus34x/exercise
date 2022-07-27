#[allow(dead_code)]
const Y: u32 = 123;
fn main() {
    // varibles
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");

    // const
    println!("The value of Y is: {Y}");

    // shadowing
    let x = 5;
    let x = x + 1;
    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
        // x= x+1;   x is immutable although it's shadowing.
    }
    println!("The value of x is: {x}");
}
