fn say_hello(name: &str) -> String {
    // We could construct the result string manually.
    // let mut result = "Hello ".to_owned();
    // result.push_str(name);
    // result.push('!');
    // result

    // But using format! is better.
    format!("Hello {}!", name)
}

fn main() {
    let s = format!("Hello {}!", "World");
    println!("s is {}", s);

    let mut t = String::from("");
    t.push_str("Hello ");
    t.push_str("World");
    println!("t is {}", t);
}
