fn main() {
    println!("Hello, world!");
    let mut v: Vec<i32> = Vec::new();
    let v1: Vec<i32> = vec![1, 2, 3];
    println!("{:?}", v1);

    // operation on vectors
    v.push(11);
    v.push(12);
    v.push(14);
    println!("{:?}", v);

    v.pop();
    match v.get(2) {
        Some(value) => println!("second element is {}", value),
            None => println!("failed to get second element of vectors"),
    }

    // iterating all the elements
    let v2 = vec![100, 32, 57];
    for i in &v2 {
        println!("{}", i);
    }
    for i in &v {
        println!("{}", i);
    }

    // enum to store different type value
    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];

}
