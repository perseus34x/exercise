fn used_function() {}

// `#[allow(dead_code)]` is an attribute that disables the `dead_code` lint
#[allow(dead_code)]
fn unused_function() {}

#[allow(dead_code)]
fn noisy_unused_function() {}
// FIXME ^ Add an attribute to suppress the warning

#[cfg(some_condition)]
fn conditional_function() {
    println!("condition met!");
}

fn main() {
    used_function();

    conditional_function();
}
