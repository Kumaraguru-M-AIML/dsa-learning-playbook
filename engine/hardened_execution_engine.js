/**
 * CQ Mythos v6.1 - Hardened Execution Infrastructure (Friction & Governance Layer)
 * 
 * Addresses the critical critique: Simulation success ≠ live market edge.
 * This engine introduces physical market constraints to dismantle the "Complexity Illusion."
 * 
 * Modules:
 * 1. Dynamic Slippage & Spread Engine (Impact of Volatility/Liquidity)
 * 2. Latency Drift Simulator (Real-world fill delays)
 * 3. Catastrophic Systemic Kill-Switch (Hard Circuit Breakers)
 */

class MarketFrictionEngine {
    /**
     * Calculates the realized execution price by injecting slippage and spread.
     * Real Edge = (Limit Price - Realized Price) > 0
     */
    static calculateRealizedFill(requestedPrice, env) {
        // Base spread is 0.02% in perfect liquid markets
        const baseSpreadPct = 0.0002; 
        
        // Volatility Spikes multiply spread exponentially
        const volatilityMultiplier = 1.0 + Math.pow(env.vix / 15.0, 1.8);
        
        // Liquidity Collapse multiplies spread exponentially
        const liquidityMultiplier = 1.0 / Math.max(env.liquidity, 0.05); 
        
        const totalSpreadPct = baseSpreadPct * volatilityMultiplier * liquidityMultiplier;
        const spreadImpact = requestedPrice * totalSpreadPct;
        
        // Random Slippage (simulating other orders hitting the book 1ms before us)
        // High Vol + Low Liquidity = High Slippage
        const maxSlippagePct = (env.vix / 100.0) * (1.0 - env.liquidity) * 0.05; 
        const randomSlippagePct = Math.random() * maxSlippagePct;
        const slippageImpact = requestedPrice * randomSlippagePct;
        
        const finalPrice = requestedPrice + spreadImpact + slippageImpact;
        
        return {
            requestedPrice,
            finalPrice,
            spreadImpact,
            slippageImpact,
            totalFrictionPercent: ((finalPrice - requestedPrice) / requestedPrice) * 100
        };
    }
}

class LatencySimulator {
    /**
     * Simulates execution delay and price movement during that window.
     * Standard internet latency + broker processing = 50ms to 800ms.
     */
    static async executeWithLatency(env) {
        // Illiquid/high-vol markets increase API queue latency
        const baseLatency = 50; // ms
        const congestionDelay = Math.floor((env.vix / 10.0) * (1.0 - env.liquidity) * 500);
        const totalLatencyMs = baseLatency + congestionDelay;
        
        console.log(`  [LATENCY] API Latency Queue: ${totalLatencyMs}ms delay injected.`);
        
        // Simulate sleep
        await new Promise(resolve => setTimeout(resolve, Math.min(totalLatencyMs, 2000)));
        
        // Simulate price drift during the delay window
        // Volatility determines the standard deviation of the drift
        const driftVolatility = (env.vix / 100.0) * (totalLatencyMs / 1000.0) * 0.02;
        const priceDriftPct = (Math.random() - 0.5) * 2.0 * driftVolatility; 
        
        return priceDriftPct;
    }
}

class KillSwitch {
    constructor(maxAllowedFrictionPct = 0.8, maxDrawdownPct = 5.0) {
        this.maxAllowedFrictionPct = maxAllowedFrictionPct; // Don't fill if slippage is too high
        this.isHalting = false;
    }

    evaluateExecutionIntegrity(frictionResult) {
        if (frictionResult.totalFrictionPercent > this.maxAllowedFrictionPct) {
            console.log(`\n\x1b[41m\x1b[37m [CRITICAL CIRCUIT BREAKER] \x1b[0m`);
            console.log(`  🚨 Realized Friction: ${frictionResult.totalFrictionPercent.toFixed(3)}% exceeded threshold ${this.maxAllowedFrictionPct}%`);
            console.log(`  🛑 [KILL-SWITCH] Order Canceled to prevent toxic fill.`);
            return false;
        }
        return true;
    }
}

class HardenedExecutionPipeline {
    constructor() {
        this.killSwitch = new KillSwitch(0.5); // Maximum 0.5% absolute friction allowed
    }

    async processOrder(ticker, requestedPrice, quantity, env) {
        console.log("\n" + "#".repeat(65));
        console.log(` 🚀 [HARDENED EXECUTION] ORDER INITIATED -> BUY ${quantity} ${ticker}`);
        console.log("#".repeat(65));
        
        console.log(`  Requested Entry: $${requestedPrice.toFixed(2)}`);
        
        // Step 1: Latency Injection & In-Flight Price Drift
        const driftPct = await LatencySimulator.executeWithLatency(env);
        const currentPriceAtBroker = requestedPrice * (1.0 + driftPct);
        console.log(`  ├─ In-Flight Price Drift: ${(driftPct * 100).toFixed(4)}%`);
        console.log(`  ├─ Broker Arrival Price: $${currentPriceAtBroker.toFixed(2)}`);

        // Step 2: Calculate Spread and Order Book Slippage
        const fillDetails = MarketFrictionEngine.calculateRealizedFill(currentPriceAtBroker, env);
        
        console.log(`  ├─ Spread Impact: +$${fillDetails.spreadImpact.toFixed(4)}`);
        console.log(`  ├─ Book Slippage: +$${fillDetails.slippageImpact.toFixed(4)}`);
        console.log(`  ├─ TOTAL FRICTION: ${fillDetails.totalFrictionPercent.toFixed(4)}%`);
        console.log(`  └─ Realized Execution Price: \x1b[33m$${fillDetails.finalPrice.toFixed(2)}\x1b[0m`);
        
        // Step 3: Circuit Breaker Check
        const isValidFill = this.killSwitch.evaluateExecutionIntegrity(fillDetails);
        
        if (!isValidFill) {
            return { status: "CANCELED", reason: "Toxic Fill / High Slippage" };
        }

        const theoreticalCost = requestedPrice * quantity;
        const physicalCost = fillDetails.finalPrice * quantity;
        const hiddenLoss = physicalCost - theoreticalCost;

        console.log(`\n🎯 \x1b[32m[ORDER FILLED SUCCESSFULLY]\x1b[0m`);
        console.log(`  ├─ Theoretical Cost: $${theoreticalCost.toFixed(2)}`);
        console.log(`  ├─ Actual Realized Cost: $${physicalCost.toFixed(2)}`);
        console.log(`  └─ \x1b[31mEdge Lost to Friction: -$${hiddenLoss.toFixed(2)}\x1b[0m\n`);

        return {
            status: "FILLED",
            ticker,
            fillPrice: fillDetails.finalPrice,
            frictionCost: hiddenLoss
        };
    }
}

// --- CRITICAL FRICTION SIMULATION ---
const pipeline = new HardenedExecutionPipeline();

async function runStressTest() {
    console.log("\x1b[36m[INITIATING REAL EXECUTION STRESS TEST (DISMANTLING COMPLEXITY ILLUSION)]\x1b[0m");

    // SCENARIO 1: Normal Market, deep liquidity
    const envNormal = { vix: 15.0, liquidity: 0.95 };
    await pipeline.processOrder("NVDA", 125.50, 66, envNormal);

    // SCENARIO 2: Fast Market, rising volatility (e.g. Post-Earnings)
    const envFast = { vix: 28.0, liquidity: 0.60 };
    await pipeline.processOrder("NVDA", 125.50, 66, envFast);

    // SCENARIO 3: Systemic Chaos (Flash Crash / High Volatility / Illiquid)
    const envCrisis = { vix: 42.0, liquidity: 0.15 };
    await pipeline.processOrder("NVDA", 125.50, 66, envCrisis);
}

runStressTest();
