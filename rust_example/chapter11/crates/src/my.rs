pub fn public_function() {
    println!("called my's `public_function()`");
}

fn private_function() {
    println!("called my's `private_function()`");
}

pub fn indirect_access() {
    print!("called my's `indirect_access()`, that\n> ");

    private_function();
}
