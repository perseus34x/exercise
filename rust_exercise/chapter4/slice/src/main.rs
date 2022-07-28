fn main() {
    println!("Hello, world!");

    let s = String::from("hello world");
    let word_number = first_word_number(&s);
    let word = first_word(&s); // word will get the value 5
    println!("there is {word_number} letters in \"{word}\"");

}

fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}

fn first_word_number(s: &String) -> usize {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
    }

    s.len()
}
