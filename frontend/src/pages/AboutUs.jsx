function AboutUs() {
    return (
      <div className="p-10 space-y-10">
        <section className="text-center">
          <h1 className="text-4xl font-bold text-yellow-300 mb-4">About Us</h1>
          <p className="text-lg max-w-3xl mx-auto">
            We are a passionate team of developers and legal experts working together to simplify legal analytics through technology and innovation.
          </p>
        </section>
  
        <section className="bg-gray-800 p-6 rounded-lg shadow-lg">
          <h2 className="text-3xl font-semibold text-yellow-300 mb-4">Our Mission</h2>
          <p>
            To bridge the gap between technology and law, empowering legal professionals with data-driven insights to make informed decisions.
          </p>
        </section>
  
        <section className="bg-gray-800 p-6 rounded-lg shadow-lg">
          <h2 className="text-3xl font-semibold text-yellow-300 mb-4">Our Vision</h2>
          <p>
            To become the leading platform for legal case prediction, helping justice move faster and more accurately through AI-powered insights.
          </p>
        </section>
  
        <section className="bg-gray-800 p-6 rounded-lg shadow-lg">
          <h2 className="text-3xl font-semibold text-yellow-300 mb-4">Core Values</h2>
          <ul className="list-disc pl-6 space-y-2">
            <li>Accuracy & Integrity</li>
            <li>User-Centric Innovation</li>
            <li>Transparency & Trust</li>
            <li>Continuous Improvement</li>
          </ul>
        </section>
  
        <section className="text-center">
          <h2 className="text-3xl font-semibold text-yellow-300 mb-4">Meet the Team</h2>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div className="bg-gray-600 p-4 rounded-lg shadow-md">
              <h3 className="text-2xl font-bold">Vivek Subramanian</h3>
              <p className="text-yellow-300">Machine Learning Expert</p>
            </div>
            <div className="bg-gray-600 p-4 rounded-lg shadow-md">
              <h3 className="text-2xl font-bold">Suman Adhithya</h3>
              <p className="text-yellow-300">Lead Developer</p>
            </div>
            <div className="bg-gray-600 p-4 rounded-lg shadow-md">
              <h3 className="text-2xl font-bold">Sri Chinnadurai</h3>
              <p className="text-yellow-300">Chief Tester</p>
            </div>
            <div className="bg-gray-600 p-4 rounded-lg shadow-md">
              <h3 className="text-2xl font-bold">Pavin Cletus</h3>
              <p className="text-yellow-300">UI/UX designer</p>
            </div>
          </div>
        </section>
      </div>
    );
  }
  
  export default AboutUs;
  