use std::arch::asm;

fn main() {
    let i: u64 = 3;
    let o: u64;
    let mut y: u64 = 3;

    println!("Hello, world!");
    let x: u64;
    unsafe {
        asm!("nop");
        asm!("mov {0}, 5", out(reg) x);

        asm!(
            "mov {0}, {1}", "add {0}, 5",
            out(reg) o, in(reg) i,
            );

        asm!("add {0}, 5", inout(reg) y);
        

    }
    assert_eq!(x, 5);
    println!("o is {}", o);
    println!("y is {}", y);
}
