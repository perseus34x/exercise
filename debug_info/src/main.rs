use env_logger::{Builder, Env};
pub use log::{debug, error, info, log_enabled, trace, warn, Level};

#[derive(Debug)]
pub struct Rectangle {
    width: u8,
    height: u64,
}

pub mod prelude {
    pub use log::{debug, error, info, log_enabled, trace, warn, Level};
}

pub fn init() -> Rectangle {
    let a: u8 = 1;
    let b: u64 = 2;
    Rectangle {
        width: a,
        height: b,
    }
}
fn main() {
    let _ = Builder::from_env(Env::default().default_filter_or("debug")).try_init();
    info!("This record will be captured by `cargo test`");
    debug!("This record will be captured by `cargo test`");
    warn!("This record will be captured by `cargo test`");
    trace!("This record will be captured by `cargo test`");
    println!("Hello, world!");

    let m = init();
    println!("width is {}, height is {}", m.width, m.height);

    let mut x = 7u64;
    println!("x is {}", x);
    let y = &mut x;
    *y =8;
    println!("y is {}", y);
    println!("x is {}", x);
}
