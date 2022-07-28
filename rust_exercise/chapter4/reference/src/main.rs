fn main() {
    let mut s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);

    // Borrow
    change(&mut s1);
    println!("The length of '{}' is {}.", s1, len);


    let s2 = &mut s1;
    println!("s2 is  {s2}.");
    let s3 = &mut s1;
    println!("s3 is  {s3}.");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);

}

fn calculate_length(s: &String) -> usize {
    s.len()
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
