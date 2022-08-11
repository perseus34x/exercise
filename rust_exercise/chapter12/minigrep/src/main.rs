use std::env;
use std::process;
use minigrep::Config;

fn main() {
    // parser input parameters
    let args: Vec<String> = env::args().collect();
    //let config = parse_config(&args);
    let config = Config::new(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {}", err);
        process::exit(1);
    });

    // read content by run.
    if let Err(e) = minigrep::run(&config) {
        eprintln!("Application error: {}", e);
        process::exit(1);
    }
}

