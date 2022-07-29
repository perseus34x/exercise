struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    // struct
    let mut user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };
    user1.email = String::from("anotheremail@example.com");

    let user2 = User {
        email: String::from("another@example.com"),
        ..user1
    };
    println!("active is {}", user1.active);
    // the string is borrowed already.
    //println!("username is {}", user1.username);

    // tuple struct
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
    println!("{}", black.0);


    // unit-like structs
    struct AlwaysEqual1;
    struct AlwaysEqual2;

    let subject1 = AlwaysEqual1;
    let subject2 = AlwaysEqual2;
    if (subject1 == subject2) {
        println!("always equal");
    }
}

fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}
