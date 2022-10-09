fn main() {
    let turing = Some("Turing");
    let logicians = vec!["Curry", "Kleene", "Markov"];

    for logician in logicians.iter().chain(turing.iter()) {
        println!("{} is a logician", logician);
    }
}
