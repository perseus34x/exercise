use std::fmt::Display;

// A trait which implements the print marker: `{:?}`.
use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

impl HasArea for Rectangle {
    fn area(&self) -> f64 { self.length * self.height }
}
impl HasArea for Triangle {
    fn area(&self) -> f64 { 0.5 * self.length * self.height }
}

#[derive(Debug)]
struct Rectangle { length: f64, height: f64 }
#[derive(Debug)]
struct Triangle  { length: f64, height: f64 }

// The generic `T` must implement `Debug`. Regardless
// of the type, this will work properly.
fn print_debug<T>(t: &T) where T: Debug {
    println!("{:?}", t);
}

// `T` must implement `HasArea`. Any type which meets
// the bound can access `HasArea`'s function `area`.
fn area<T>(t: &T) -> f64 where T: HasArea { t.area() }

// Define a function `printer` that takes a generic type `T` which
// must implement trait `Display`.
fn printer<T>(t: T) where T: Display {
    println!("{}", t);
}

fn main() {
    printer("a");
//    printer(vec![2]);

    let rectangle = Rectangle { length: 3.0, height: 4.0 };
    let _triangle = Triangle  { length: 3.0, height: 4.0 };
    print_debug(&rectangle);
    println!("Area: {}", rectangle.area());

    print_debug(&_triangle);
    println!("Area: {}", area(&_triangle));
}
