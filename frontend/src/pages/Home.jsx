const Home = () => {
    return (
      <div className="p-10 space-y-16">
        <section className="text-center">
          <h1 className="text-4xl font-bold text-yellow-300 mb-4">Empowering Legal Decisions with AI</h1>
          <p className="text-lg text-gray-300">Lawgorithm helps predict case outcomes through advanced machine learning models.</p>
        </section>
  
        <section className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="p-6 bg-gray-800 rounded-lg shadow-md">
            <h2 className="text-2xl font-semibold text-yellow-300 mb-2">Why Lawgorithm?</h2>
            <p className="text-gray-300">We combine legal expertise with technology to deliver insights that help lawyers make better decisions.</p>
          </div>
          <div className="p-6 bg-gray-800 rounded-lg shadow-md">
            <h2 className="text-2xl font-semibold text-yellow-300 mb-2">Fast & Accurate Predictions</h2>
            <p className="text-gray-300">Get reliable case outcome predictions in seconds by submitting your case summary.</p>
          </div>
        </section>
  
        <section className="text-center">
          <button 
            className="bg-yellow-400 text-gray-900 px-6 py-3 rounded-lg font-bold hover:bg-yellow-300 transition"
            onClick={() => window.location.href='/predict'}
          >
            Access the Model
          </button>
        </section>
      </div>
    );
  };
  
  export default Home;
  