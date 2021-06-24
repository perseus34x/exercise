fn main() {
    println!("Hello, world!");
    println!("I'm a Rustacean");

    let x = 5 + /* 90 + */ 5;
    println!("Is `x` 10 or 100? x = {}", x);

    println!("{} days", 31i64);
    
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

}
