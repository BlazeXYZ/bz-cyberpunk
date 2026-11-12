package syntax_tests;

import java.util.*;
import java.util.function.Function;
import static java.lang.Math.max;
import static java.util.Objects.requireNonNull;

/**
 * A Java syntax highlighting test.
 * <p>
 * Open this file with the theme active to check every Java color.
 *
 * @param <T> the payload type
 * @author BlazeXYZ
 * @see <a href="https://www.cyberpunk.net">Night City</a>
 */
@SuppressWarnings({"unused", "FieldMayBeFinal"})
public sealed abstract class JavaSyntax<T extends Comparable<T>> permits JavaSyntax.Netrunner {

    public static final int MAX_RAM = 0x2077;          // static final field (constant)
    private static String fixer = "Rogue";              // static field
    protected final List<T> implants = new ArrayList<>(); // instance final field
    private double eddies = 1_000.50d;                  // instance field
    private char glyph = '█';
    private String broken = "Bad escape: \q and good: \n\t";

    enum Faction { ARASAKA, MILITECH, MAELSTROM }

    record Gig(String client, int payout) implements Comparable<Gig> {
        @Override
        public int compareTo(Gig other) {
            return Integer.compare(payout, other.payout);
        }
    }

    interface Daemon {
        void upload(String target) throws IllegalStateException;
    }

    abstract void jackIn(int port);

    static final class Netrunner extends JavaSyntax<String> implements Daemon {
        @Override
        void jackIn(int port) {
            int retries = 3;
            retries--;                                 // reassigned local variable
            label:
            for (int i = 0; i < retries; i++) {
                if (i == MAX_RAM) break label;
                upload("port:" + port);
            }
        }

        @Override
        public void upload(String target) {
            var text = """
                    Wake up, choom.
                    We have a city to burn.
                    """;
            Function<String, Integer> len = s -> s.length();   // lambda parameter
            Daemon anon = new Daemon() {
                @Override
                public void upload(String t) {
                    System.out.println(target + t);           // captured variable
                }
            };
            anon.upload(text);
            System.out.println(max(len.apply(target), MAX_RAM));
            requireNonNull(fixer);
            Object o = Faction.ARASAKA;
            String result = switch (o) {
                case Faction f when f == Faction.MILITECH -> "corpo";
                case Faction f -> f.name().toLowerCase();
                default -> throw new IllegalArgumentException();
            };
            // TODO: flatline the ICE before the Blackwall notices
            undefinedSymbol();                                 // unresolved reference
        }

        @Deprecated(forRemoval = true)
        void legacyDeck() { }

        @Deprecated
        void oldDeck() {
            legacyDeck();
            oldDeck();
        }
    }
}
