fn main() {

    println!("=========== Chpter1 Hello world=========");
    // comments
    println!("=========== comments =========");
    let x = 5 + /* 90 + */ 5;
    println!("Is `x` 10 or 100? x = {}", x);

    println!();
    //Print Format
    println!("=========== Print =========");
    println!("Hello, world! I'm a Rustacean");
    println!("{} days", 32i64);
    
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");

    println!("{subject} {verb} {object}",
             object = "the lazy dog",
             subject = "the quick brown fox",
             verb = "jump over");

    println!("{} of 0b{:04b} people know binary, the other half doestn't", 1, 2);

    println!("{number:>width$}", number=2, width=8);

    println!("my name is {0}, {1} {0}", "Bond", "James");

    #[derive(Debug)]
    struct Structure(i32);
    println!("This struct `{:?}` won't print...", Structure(3));

    let pi = 3.141592;
    println!("Pi is roughly {1:.0$}",  3, pi);
    println!("Pi is roughly {:.*}",  4, pi);

    #[derive(Debug)]
    struct Structure1(i32);
    #[derive(Debug)]
    struct Deep(Structure1);
    println!("Now {:?} will print.", Structure1(3));
    println!("Now {:?} will pirnt.", Deep(Structure1(7)));

    #[derive(Debug)]
    #[allow(dead_code)]
    struct Person<'a> {
        name : &'a str,
        age  : u8
    }
    let name = "Peter";
    let age = 18;
    let peter = Person{name, age};
    println!("{:#?}", peter);

    use std::fmt;
    struct Structure2(i32);
    impl fmt::Display for Structure2 {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            write!(f, "{}", self.0)
        }
    }

    #[derive(Debug)]
    struct MinMax(i64, i64);
    impl fmt::Display for MinMax {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            write!(f, "({}, {})", self.0, self.1)
        }
    }

    #[derive(Debug)]
    struct Point2D {
        x: f64,
        y: f64,
    }
    impl fmt::Display for Point2D {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            write!(f, "x: {}, y: {}", self.x, self.y)
        }
    }

    let minmax = MinMax(0, 14);
    println!("Display {}", minmax);
    println!("Debug: {:?}", minmax);

    let big_range = MinMax(-300, 300);
    let small_range = MinMax(-3, 3);
    println!("The big range is {big} and the small is {small}",
             small = small_range,
             big = big_range);

    let point = Point2D {x: 3.3, y: 7.2};
    println!("compare points:");
    println!("Display: {}", point);
    println!("Debug: {:?}", point);
    println!("Display: {} + {}i", point.x, point.y);
    println!("Debug: Complex {{real: {real}, imag: {image} }}", real=point.x, image=point.y);
}
