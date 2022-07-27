fn main() {
    println!("Hello, world!");
    let y = another_function(5, 'd');

    // statement
    let _x = 6;
    println!("y is {y}");
}
fn another_function (x: u32, unit: char) -> u32 {
    println!("call another functions for {x}{unit}");
    let y: u32 = {
        let x = 4;
        x+1
    };
    return y;
}
