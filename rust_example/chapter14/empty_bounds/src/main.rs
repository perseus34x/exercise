struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}
impl Red for Turkey {}

// These functions are only valid for types which implement these
// traits. The fact that the traits are empty is irrelevant.
fn red<T>(_: &T)   -> &'static str where T: Red { "red" }
fn blue<T>(_: &T) -> &'static str where T: Blue { "blue" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let turkey   = Turkey;

    // `red()` won't work on a blue jay nor vice versa
    // because of the bounds.
    println!("A cardinal is {}", red(&cardinal));
    println!("A blue jay is {}", blue(&blue_jay));
    println!("A turkey is {}", red(&turkey));
    // ^ TODO: Try uncommenting this line.
}

