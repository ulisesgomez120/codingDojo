var users = [
    {name: "Michael", age:37}, 
    {name: "John", age:30}, 
    {name: "David", age:27}
];
//john's age
console.log(users[1].age); //I had logged his name by mistake
//first obj
console.log(users[0].name);
//loop
for(var i = 0; i < users.length; i++) {
    console.log(users[i].name + " - " + users[i].age);
}