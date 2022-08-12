use std::error::Error;
use std::fs;
use std:: env;

pub struct Config {
    query: String,
    filename: String,
    ignore_case: bool,
}

impl<'a> Config {
    pub fn new (mut args: impl Iterator<Item = String>
        ) -> Result<Config, &'static str> {

        args.next();
        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let filename = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file name"),
        };
        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {query, filename, ignore_case})
    }
}

pub fn run(config: &Config) -> Result<(), Box<dyn Error>> {
    println!("Searching for {}", config.query);
    println!("In file {}", config.filename);
    println!("\r");

    let contents = fs::read_to_string(&config.filename)?;
    let result = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };
    for line in result {
        println!("{}", line);
    }
    Ok(())
}

pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    contents.lines().filter(|line| line.contains(query)).collect()
}

pub fn search_case_insensitive<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    contents.lines().filter(|line| line.to_lowercase().contains(&query)).collect()
}
