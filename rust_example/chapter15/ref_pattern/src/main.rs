#[derive(Clone, Copy)]
struct Point { x: i32, y: i32 }
struct Point1 { x: i32, y: String }

fn main() {
    let c = 'Q';

    // A `ref` borrow on the left side of an assignment is equivalent to
    // an `&` borrow on the right side.
    let ref ref_c1 = c;
    let ref ref_c2 = &c;
    println!("ref_c1 equals ref_c2: {}", ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };
    // `ref` is also valid when destructuring a struct.
    let _copy_of_x = {
        // `ref_to_x` is a reference to the `x` field of `point`.
        let Point { x: ref ref_to_x, y: _ } = point;

        // Return a copy of the `x` field of `point`.
        *ref_to_x
    };

    // A mutable copy of `point`
    let mut mutable_point = point;
    {
        // `ref` can be paired with `mut` to take mutable references.
        let Point { x: _, y: ref mut mut_ref_to_y } = mutable_point;

        // Mutate the `y` field of `mutable_point` via a mutable reference.
        *mut_ref_to_y = 1;
    }
    println!("point is ({}, {})", point.x, point.y);
    println!("mutable_point is ({}, {})", mutable_point.x, mutable_point.y);

    let point1 = Point1 {x: 10, y: String::from("xyz")};
    let mut mutable_point1 = point1;
    //println!("point is ({}, {})", point1.x, point1.y);
    println!("mutable_point is ({}, {})", mutable_point1.x, mutable_point1.y);

    // A mutable tuple that includes a pointer
    let mut mutable_tuple = (Box::new(5u32), 3u32);
    {
        // Destructure `mutable_tuple` to change the value of `last`.
        let (mut first, ref mut last) = mutable_tuple;
        *last = 2u32;
        first = Box::new(6u32);
        println!("tuple is {:?}", first);
    }
    //println!("tuple is {:?}", mutable_tuple);
    println!("tuple is {:?}", mutable_tuple.1);

}
