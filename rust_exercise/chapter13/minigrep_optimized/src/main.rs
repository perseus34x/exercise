use std::env;
use std::process;
use minigrep_optimized::Config;

fn main() {
    // parser input parameters
    //let args: Vec<String> = env::args().collect();
    let config = Config::new(env::args()).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {}", err);
        process::exit(1);
    });

    // read content by run.
    if let Err(e) = minigrep_optimized::run(&config) {
        eprintln!("Application error: {}", e);
        process::exit(1);
    }
}
