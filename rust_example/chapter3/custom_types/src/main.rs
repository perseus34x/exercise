// An attribute to hide warnings for unused code.
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// A unit struct
struct Unit;

// A tuple struct
struct Pair(i32, f32);

// A struct with two fields
struct Point {
    x: f32,
    y: f32,
}

// Structs can be reused as fields of another struct
struct Rectangle {
    // A rectangle can be specified by where the top left and bottom right
    // corners are in space.
    top_left: Point,
    bottom_right: Point,
}

fn main() {

    println!("===================== Structures ====================="); 
    // Create struct with field init shorthand
    let name = String::from("Peter");
    let age = 27;
    let peter = Person{name, age};
    println!("{:?}", peter);

    // Instantiate a `Point`
    let point: Point = Point{x: 10.3, y: 0.4};
    // Access the fields of the point
    println!("point coordinates: ({}, {})", point.x, point.y);

    // Make a new point by using struct update syntax to use the fields of our
    // other one
    let bottom_right = Point{x: 20.3, ..point};
    println!("point coordinates: ({}, {})", bottom_right.x, bottom_right.y);

    // Destructure the point using a `let` binding
    let Point { x:left_edge, y:top_edge } = point;
    println!("{}, {}", left_edge, top_edge);
    let top_edge = 1.4;

    let _rectangle = Rectangle {
        top_left: Point{x: left_edge, y: top_edge},
        bottom_right: bottom_right,
    };

    // Instantiate a unit struct
    let _unit = Unit;

    // Instantiate a tuple struct
    let pair = Pair(1, 0.1);
    // Access the fields of a tuple struct
    println!("pair contains {:?} and {:?}", pair.0, pair.1);

    // Destructure a tuple struct
    let Pair(integer, decimal) = pair;
    println!("pair contains {:?} and {:?}", integer, decimal);

    let area = rect_area(_rectangle);
    println!("area of rect is {}", area);

    let sqr = square(point, 1.0);
    println!("area of sqr is {}", rect_area(sqr));


    println!("===================== Enums ====================="); 
    let pressed = WebEvent::KeyPress('x');
    // `to_owned()` creates an owned `String` from a string slice.
    let pasted  = WebEvent::Paste("my text".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let load    = WebEvent::PageLoad;
    let unload  = WebEvent::PageUnload;
    inspect(pressed);
    inspect(pasted);
    inspect(click);
    inspect(load);
    inspect(unload);

}

fn rect_area(rect: Rectangle) -> f32 {
    
    let Rectangle{top_left:Point{x:x1, y:y1},bottom_right:Point{x:x2,y:y2}} = rect;
    ((x2-x1)*(y1-y2)).abs()
}

fn square( top_left: Point, edge:f32) -> Rectangle {
    let bottom_right = Point{x:top_left.x + edge, y:top_left.y - edge};
    Rectangle{ 
      top_left: top_left, 
      bottom_right: bottom_right,
    }
}

// Create an `enum` to classify a web event. Note how both
// names and type information together specify the variant:
// `PageLoad != PageUnload` and `KeyPress(char) != Paste(String)`.
// Each is different and independent.
enum WebEvent {
    // An `enum` may either be `unit-like`,
    PageLoad,
    PageUnload,
    // like tuple structs,
    KeyPress(char),
    Paste(String),
    // or c-like structures.
    Click { x: i64, y: i64 },
}

// A function which takes a `WebEvent` enum as an argument and
// returns nothing.
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("page loaded"),
        WebEvent::PageUnload => println!("page unloaded"),
        // Destructure `c` from inside the `enum`.
        WebEvent::KeyPress(c) => println!("pressed '{}'.", c),
        WebEvent::Paste(s) => println!("pasted \"{}\".", s),
        // Destructure `Click` into `x` and `y`.
        WebEvent::Click { x, y } => {
            println!("clicked at x={}, y={}.", x, y);
        },
    }
}
