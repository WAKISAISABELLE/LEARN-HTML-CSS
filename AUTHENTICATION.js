//ISABELLE WAKISA B30311 S24B38/019

// USER AUTHENTICATION 
const fs = require("fs");  //this will allow the code ti interact with the file system.
const bcrypt = require("bcryptjs"); //this will hash the password and ensure security
const readline = require("readline-sync"); //it will allow the code to read input from the commandline

const userFile = "users.json";  //this isnwhere the user data is saved

// Loading the user data from JSON file
function loadUsers() {
  try {                    //this will define a block of code to be tested for errors
    const data = fs.readFileSync(userFile);
    return JSON.parse(data); // returns as java script object
  } catch (error) {
    return {}; // Return empty object if file doesn't exist or is empty
  }
}

// Save user data to JSON file
function saveUsers(users) {
  fs.writeFileSync(userFile, JSON.stringify(users, null, 2));  //stringify:will covert the json object into string. writeFileSync will write data to the file
}

// Register a new user
function register() {
  console.log("\n Register ");
  const username = readline.question("Enter a username: ").trim();
  if (!username) {
    console.log("Username cannot be empty.");
    return register();
  }

  const users = loadUsers();
  if (users[username]) {
    console.log("Username already exists. Try a different one.");
    return;
  }

  const password = readline.question("Enter password: ", { hideEchoBack: true }); //enter a secret text


  const hashedPassword = bcrypt.hashSync(password, 10);   
  users[username] = hashedPassword;
  saveUsers(users);
  
  console.log("Account created successfully!");
  
  // Asking if the user wants to log in
  const loginChoice = readline.question("Do you want to log in? (yes/no): ").toLowerCase();
  if (loginChoice === "yes" || loginChoice === "y") {
    login();
  } else {
    console.log("Thank you for registering! ")
  } 
}

// Login function
function login() {
  console.log("\nLogin");
  const username = readline.question("Enter your username: ").trim();
  const users = loadUsers();

  if (!users[username]) {
    console.log("User not found. Please register first.");
    return;
  }

  const password = readline.question("Enter your password: ", { hideEchoBack: true });

  if (bcrypt.compareSync(password, users[username])) {
    console.log("Login successful!");
    userMenu(username);
  } else {
    console.log("Incorrect password. Try again.");
  }
}

// User menu after login
function userMenu(username) {
  console.log(`\nWelcome, ${username}!`);
  while (true) {
    console.log("\n1. View Profile");
    console.log("2. Logout");
    const option = readline.question("Choose an option: ");

    if (option === "1") {
      console.log(`\nUsername: ${username}`);
    } else if (option === "2") {
      console.log("Logging out...\n");
      return;
    } else {
      console.log("Invalid choice. Try again.");
    }
  }
}

// We create a function for the Main menu
function mainMenu() {
  while (true) {
    console.log("\n1. Register");
    console.log("2. Login");
    console.log("3. Exit");
    const option = readline.question("Choose an option: ");

    if (option === "1") {
      register();
    } else if (option === "2") {
      login();
    } else if (option === "3") {
      console.log("Goodbye!");
      process.exit();
    } else {
      console.log("Invalid choice. Try again.");
    }
  }
}


mainMenu();
