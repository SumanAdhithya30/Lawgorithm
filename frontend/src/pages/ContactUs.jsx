function ContactUs() {
    return (
      <div className="p-10 max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold mb-6 text-yellow-300">Contact Us</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <h2 className="text-2xl font-semibold mb-4">Team Members</h2>
            <ul className="space-y-4">
              <li>
                <h3 className="text-xl font-medium">Vivek Subramanian</h3>
                <p>Email: <a href="1049viveksubramaniang@gmail.com" className="text-blue-400 hover:text-blue-300">1049viveksubramaniang@gmail.comm</a></p>
                <p>GitHub: <a href="https://github.com/Vivek-7" className="text-blue-400 hover:text-blue-300">github.com/Vivek-7</a></p>
              </li>
              <li>
                <h3 className="text-xl font-medium">Suman Adhithya</h3>
                <p>Email: <a href="mailto:sumanadhithya701@gmail.com" className="text-blue-400 hover:text-blue-300">sumanadhithya701@gmail.com</a></p>
                <p>GitHub: <a href="https://github.com/SumanAdhithya30" className="text-blue-400 hover:text-blue-300">github.com/SumanAdhithya30</a></p>
              </li>
              <li>
                <h3 className="text-xl font-medium">Sri Chinnadurai</h3>
                <p>Email: <a href="mailto:chris@example.com" className="text-blue-400 hover:text-blue-300">chris@example.com</a></p>
                <p>GitHub: <a href="https://github.com/sri chinnadurai.s" className="text-blue-400 hover:text-blue-300">github.com/sri chinnadurai.s</a></p>
              </li>
              <li>
                <h3 className="text-xl font-medium">Pavin Cletus</h3>
                <p>Email: <a href="mailto:pavincletus3@gmail.com" className="text-blue-400 hover:text-blue-300">pavincletus3@gmail.com</a></p>
                <p>GitHub: <a href="https://github.com/pavincletus3" className="text-blue-400 hover:text-blue-300">github.com/pavincletus3</a></p>
              </li>
            </ul>
          </div>
          <div>
            <h2 className="text-2xl font-semibold mb-4">Socials</h2>
            <p>GitHub: <a href="https://github.com/lawgorithm" className="text-blue-400 hover:text-blue-300">github.com/lawgorithm</a></p>
            <p>LinkedIn: <a href="https://linkedin.com/company/lawgorithm" className="text-blue-400 hover:text-blue-300">linkedin.com/company/lawgorithm</a></p>
          </div>
        </div>
      </div>
    );
  }

  export default ContactUs;
