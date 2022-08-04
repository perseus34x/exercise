fn main() {
    println!("Hello, world!");
    let s = "initial contents".to_string();
    println!("s is {}", s);
    let mut s = String::from("initial contents");
    s.push_str(" just now");
    println!("s is {}", s);

    let mut s1 = String::from("foo");
    let s2 = "bar";
    s1.push_str(&s2);
    println!("s2 is {}", s2);

    // concentrate
    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");
    let s3 = s1 + &s2; // note s1 has been moved here and can no longer be used
    println!("s3 is {}", s3);

    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let s = s1 + "-" + &s2 + "-" + &s3;
    println!("s is {}", s);

    // Indexing into Strings
    let s1 = String::from("hello");
    let h = s1[0];
    println!("h is {}", h);
}
