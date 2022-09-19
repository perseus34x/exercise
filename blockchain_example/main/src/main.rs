use core::blockchain;
use std::thread;
use std::time::Duration;

fn main() {
    let mut bc = blockchain::BlockChain::new();

    println!("Start mining...");
    thread::sleep(Duration::from_secs(2));
    bc.add_block(String::from("a -> b @5btc"));
    println!("produce a block");
    println!("");

    println!("Start mining...");
    thread::sleep(Duration::from_secs(2));
    bc.add_block(String::from("c -> d @1btc"));
    println!("produce a block");
    println!("");

    for block in bc.blocks {
        println!("++++++++++++++++++"); 
        println!("{:#?}", block); 
    }
}
